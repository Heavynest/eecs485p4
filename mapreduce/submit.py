"""
MapReduce job submission script.

Before using this script, start the MapReduce server.
$ ./bin/mapreduce start

Then, submit a job.  Everything has a default.
$ mapreduce-submit

You can change any of the options.
$ mapreduce-submit --help
"""

import socket
import json
import click


# Configure command line options
@click.command()
@click.option(
    "--port", "-p", "port", default=6000,
    help="Master port number, default = 6000",
)
@click.option(
    "--input", "-i", "input_directory", default="./input",
    help="Input directory, default=./input",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
)
@click.option(
    "--output", "-o", "output_directory", default="./output",
    help="Output directory, default=./output",
    type=click.Path(exists=False, file_okay=False, dir_okay=True),
)
@click.option(
    "--mapper", "-m", "mapper_executable", default="./exec/bash_wc/map",
    help="Mapper executable, default=./exec/bash_wc/map",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.option(
    "--reducer", "-r", "reducer_executable", default="./exec/bash_wc/reduce",
    help="Reducer executable, default=./exec/bash_wc/reduce",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
)
@click.option(
    "--nmappers", "num_mappers", default=4, type=int,
    help="Number of mappers, default=4",
)
@click.option(
    "--nreducers", "num_reducers", default=1, type=int,
    help="Number of reducers, default=1",
)
def main(port,
         input_directory,
         output_directory,
         mapper_executable,
         reducer_executable,
         num_mappers,
         num_reducers):
    """Top level command line interface."""
    # We want a bunch of arguments, this is the top level CLI.
    # pylint: disable=too-many-arguments
    job_dict = {
        "message_type": "new_master_job",
        "input_directory": input_directory,
        "output_directory": output_directory,
        "mapper_executable": mapper_executable,
        "reducer_executable": reducer_executable,
        "num_mappers": num_mappers,
        "num_reducers": num_reducers
    }

    message = json.dumps(job_dict)

    # Send the data to the port that master is on
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", port))
        sock.sendall(str.encode(message))
        sock.close()
        print("Send job to master")
    except socket.error as err:
        print("Failed to send job to master.")
        print(err)


if __name__ == "__main__":
    # Click will provide the arguments, disable this pylint check.
    # pylint: disable=no-value-for-parameter
    main()
