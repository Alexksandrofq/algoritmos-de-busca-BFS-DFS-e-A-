import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        # TODO: implemente a heurística aqui
        # Distancia Manhattan: o vazio nao participa da estimativa.
        distance = 0
        for index, tile in enumerate(state.tiles):
            if tile != 0:
                row, col = divmod(index, 3)
                goal_row, goal_col = divmod(tile - 1, 3)
                distance += abs(row - goal_row) + abs(col - goal_col)
        return distance
        raise NotImplementedError

    def search(self, initial: State) -> SearchResult:
        # TODO: implemente o A* aqui
        sequence = 0
        frontier = [(initial.cost + self.heuristic(initial), sequence, initial, 0)]
        best_cost = {initial.tiles: initial.cost}
        result = SearchResult(solution=None, nodes_generated=1, max_frontier_size=1)

        while frontier:
            _, _, state, depth = heapq.heappop(frontier)
            if state.cost != best_cost[state.tiles]:
                continue
            if state.is_goal:
                result.solution = state
                result.depth = depth
                return result

            result.nodes_expanded += 1
            for child in state.neighbors():
                result.nodes_generated += 1
                if child.cost < best_cost.get(child.tiles, float("inf")):
                    best_cost[child.tiles] = child.cost
                    sequence += 1
                    heapq.heappush(frontier, (
                        child.cost + self.heuristic(child), sequence, child, depth + 1,
                    ))
            result.max_frontier_size = max(result.max_frontier_size, len(frontier))

        return result
        raise NotImplementedError
