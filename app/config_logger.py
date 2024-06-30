import logging
import randomname

def configure_logging(logger: logging.Logger, suffix: str):
    """
    Configures the passed logger, to write to a randomly generated filename in /tmp/, and also output log messages to the terminal
    The terminal messages should normally be sufficient, but the file will be useful if the number of messages is high
    The generated filename is also printed out

    :param logging.Logger logger: the logger
    :param str suffix: a keyword to denote what part of the solution we're logging.
        Helpful to differentiate the publisher logs vs the subscriber logs. Will be included in the filename
    """

    filename = f"/tmp/mongo-pubsub-{suffix}-{randomname.get_name()}.log"
    logging.basicConfig(filename=filename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    
    # Create a handler for printing to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set console output to a desired level

    # Define a formatter for console output
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the root logger
    logging.getLogger('').addHandler(console_handler)

    logging.info("Created logfile: " + filename)