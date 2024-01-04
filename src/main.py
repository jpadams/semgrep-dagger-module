from datetime import datetime
import dagger
from dagger import dag, function

@function
async def scan(source: dagger.Directory) -> str:
    # Example usage: "dagger call scan --source .
    return await (
        dag.container()
        .from_("returntocorp/semgrep")
        .with_mounted_directory("/src", source)
        .with_workdir("/src")
		.with_env_variable("CACHEBUSTER", str(datetime.now()))
        .with_exec(["semgrep", "scan", "--verbose"])
        .stdout()
    )
