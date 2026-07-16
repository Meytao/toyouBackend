from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import AsyncSessionLocal
from app.models.nav_item import NavItem

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
    """初始化所有数据"""
    async with AsyncSessionLocal() as session:
        try:
            await init_nav_item_data(session)
        finally:
            await session.close()
