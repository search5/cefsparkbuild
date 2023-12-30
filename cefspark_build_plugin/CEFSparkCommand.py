from cleo.commands.command import Command
from cleo.io.inputs.argument import Argument
from cleo.io.inputs.option import Option
from poetry.plugins.application_plugin import ApplicationPlugin


class CEFSparkCommand(Command):
    name = "cefspark-command"
    description = "Command Helper"

    help = "Command Helper help~"
    # arguments = "cleo.io.inputs.argument.Argument"
    arguments = [Argument("data", False, True, '데해햇')]
    options = [Option("--data", '-d', True)]
    # name: str,
    #         required: bool = True,
    #         is_list: bool = False,
    #         description: str | None = None,
    #         default: Any | None = None,

    # options = "cleo.io.inputs.option.Option"
    # usages = ""

    def handle(self) -> int:
        self.line("My command")

        print(self.argument('data'))

        return 0


def factory():
    return CEFSparkCommand()

class CEFSparkCommand2(Command):
    """Command2 Helper"""
    name = "cefspark-command2"

    def handle(self) -> int:
        self.line("My command")
        print(dir(self))

        return 0


def factory2():
    return CEFSparkCommand2()

class CEFSparkPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("cefspark-command", factory)
        application.command_loader.register_factory("cefspark-command2", factory2)
