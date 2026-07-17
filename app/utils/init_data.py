import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import AsyncSessionLocal
from app.models.nav_item import NavItem
from app.models.setting import Setting

logger = logging.getLogger(__name__)
DEFAULT_NAV_ITEMS = [
    {"name": "setup", "path": "/setup", "title": "初始化", "icon": "🔧", "sort_order": 0},
    {"name": "Home", "path": "/", "title": "首页", "icon": "🏠", "sort_order": 1},
    {"name": "Posts", "path": "/posts", "title": "文章", "icon": "📝", "sort_order": 2},
    {"name": "Moments", "path": "/moments", "title": "朋友圈", "icon": "💬", "sort_order": 3},
    {"name": "Treasure", "path": "/treasure", "title": "百宝箱", "icon": "🎁", "sort_order": 4},
    {"name": "Friends", "path": "/friends", "title": "友链", "icon": "🔗", "sort_order": 5},
    {"name": "About", "path": "/about", "title": "关于", "icon": "👤", "sort_order": 6},
    {"name": "RSS", "path": "/rss", "title": "RSS", "icon": "📡", "sort_order": 7},
]


async def check_is_initialized(db: AsyncSession) -> bool:
    """检查系统是否已经初始化"""
    result = await db.execute(
        select(Setting).where(Setting.key == "is_initialized")
    )
    setting = result.scalar_one_or_none()
    if setting is None:
        return False
    return setting.value == "true"


async def set_initialized(db: AsyncSession):
    """标记系统已初始化"""
    result = await db.execute(
        select(Setting).where(Setting.key == "is_initialized")
    )
    setting = result.scalar_one_or_none()
    if setting is None:
        db.add(Setting(key="is_initialized", value="true"))
    else:
        setting.value = "true"
    await db.commit()


async def init_nav_item_data(db: AsyncSession):
    for item in DEFAULT_NAV_ITEMS:
        result = await db.execute(
            select(NavItem).where(NavItem.name == item["name"])
        )
        exists = result.scalar_one_or_none()
        if not exists:
            db.add(NavItem(
                name=item["name"],
                path=item["path"],
                title=item["title"],
                icon=item["icon"],
                sort_order=item["sort_order"],
                parent_id=0,
                status=1,
                is_hidden=0,
            ))
    await db.commit()


async def init_all_data():
    """初始化所有数据（仅执行一次）"""
    async with AsyncSessionLocal() as session:
        try:
            is_initialized = await check_is_initialized(session)
            if is_initialized:
                logger.info("系统已初始化，跳过数据初始化")
                return

            logger.info("开始初始化系统数据...")
            await init_nav_item_data(session)
            await set_initialized(session)
            logger.info("系统数据初始化完成")
        finally:
            await session.close()
