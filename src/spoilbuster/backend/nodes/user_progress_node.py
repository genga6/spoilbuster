from spoilbuster.backend.core.node import Node

class UserProgressNode(Node):
    def __init__(
        self, 
        input_key: list[str], 
        output_key: list[str],
    ):
        super().__init__(input_key, output_key)


    def execute(self, state) -> dict:
        pass    #TODO: 抽象的に分類し、プレイヤーの進行状況でネタバレの判断材料を提供