# Учитывая m x nдвумерную двоичную сетку grid, которая представляет карту '1's (суша) и '0's (вода),
# верните число островов .

# Остров окружен водой и образован путем соединения соседних земель по горизонтали или вертикали.
# Вы можете предположить, что все четыре края сетки окружены водой.

# Рассмотрим каждую ячейку. Если это остров (1) запускаем поиск в глубину, чтобы осмотреться вправо, влево, вверх и вниз

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0  
            
        count = 0 #рассмотрим значение для каждой
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)