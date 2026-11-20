from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:
        # TODO: implemente a DFS aqui
        frontier = [(initial, 0)]
        # Uma chegada mais rasa permite explorar caminhos antes cortados pelo limite.
        best_depth = {initial.tiles: 0}
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            state, depth = frontier.pop()
            if depth != best_depth[state.tiles]:
                continue
            if state.is_goal:
                result.solution = state
                result.depth = depth
                return result
            if depth >= self.depth_limit:
                continue

            result.nodes_expanded += 1
            children = state.neighbors()
            result.nodes_generated += len(children)
            # A pilha visita primeiro o primeiro movimento retornado por neighbors.
            for child in reversed(children):
                child_depth = depth + 1
                if child_depth < best_depth.get(child.tiles, float("inf")):
                    best_depth[child.tiles] = child_depth
                    frontier.append((child, child_depth))
            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
        raise NotImplementedError("Implemente o método search na classe DFS.")
