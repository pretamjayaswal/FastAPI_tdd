

from typing import List, Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url = payload.url,
        summary = "This is dummy summary"
    )
    await summary.save()
    return summary.id

async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    # print(summaries)
    if summaries:
        return summaries
    return None

async def delete(id: int) -> Union[int, None]:
    summary = await TextSummary.filter(id=id).first()
    if summary:
        id = summary.id
        summary.delete()
        return id
        
    return None
