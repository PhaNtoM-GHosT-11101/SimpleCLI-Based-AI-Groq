import os
from dotenv import load_dotenv
from groq import Groq
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.markdown import Markdown
from rich.spinner import Spinner
from rich.align import Align

load_dotenv()
console = Console()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# auto-pick live model
MODEL = client.models.list().data[0].id

console.print(Panel.fit("[bold green]Groq Terminal Brain Online[/bold green]\nType 'exit' to quit"))

while True:
    user = console.input("[bold yellow]You › [/bold yellow]")
    if user.lower() in ("exit","quit"):
        break

    with Live(Spinner("dots", text="Thinking at warp speed..."), refresh_per_second=12):
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role":"user","content":user}]
        )

    answer = resp.choices[0].message.content

    console.print(Panel(Markdown(answer), title="[cyan]AI[/cyan]", border_style="cyan"))
