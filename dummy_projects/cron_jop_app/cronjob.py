from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
import uvicorn

counter = 1


def job_counter():
    global counter
    print(f"counter: {counter}")
    counter += 1


@asynccontextmanager
async def lifespan(_: FastAPI):
    print("app started.")
    scheduler = BackgroundScheduler()
    # trigger type bilgisi cron time  komutları ile verilebiliyor.
    # scheduler.add_job(id="job1", func=job_counter, trigger="interval", seconds=1)
    scheduler.add_job(id="job1", func=job_counter, trigger="cron", year='*', month='*', day='*', week='*',
                      day_of_week='*', hour='*', minute='*', second='*')
    scheduler.start()
    yield
    print("app stopped.")
    scheduler.shutdown(wait=False)


app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run("cronjob:app")
