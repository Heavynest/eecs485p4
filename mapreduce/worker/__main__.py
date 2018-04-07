import click, time
import mapreduce.helper as helper

class Worker:
    # TODO
    pass

@click.command()
@click.argument("master_port_num", nargs=1, type=int)
@click.argument("worker_port_num", nargs=1, type=int)
def main(master_port_num, worker_port_num):
    print("This is where you implement Worker!")
    # TODO: you should remove this. This is just so the program doesn't 
    #       exit immediately!
    time.sleep(120)

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
