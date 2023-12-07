from prefect import flow
from prefect_shell import shell_run_command


@flow
def example_shell_run_command_flow():
    return shell_run_command(command="mlserver start .", return_all=True)


if __name__ == "__main__":
    example_shell_run_command_flow()