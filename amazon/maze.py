# public static boolean maze(int[][] m) {
# 		if(m == null || m.length == 0 || m[0][0] == 0) return false;
# 		int w = m[0].length, h = m.length;
# 		return dfs(m, 0, 0, w, h);
# 	}
# 	public static boolean dfs(int[][] m, int i, int j, int w, int h) {
# 		if(i > h - 1 || j > w - 1 || i < 0 || j < 0 || m[i][j] == 0 || m[i][j] == 2) return false;
# 		if(m[i][j] == 9) {
# 			System.out.println("99999");
# 			return true;
# 		}
# 		m[i][j] = 2;
# 		boolean left = dfs(m, i, j - 1, w, h);
# 		boolean right = dfs(m, i, j + 1, w, h);
# 		boolean up = dfs(m, i - 1, j, w, h);
# 		boolean down = dfs(m, i + 1, j, w, h);
# 		m[i][j] = 1;
# 		return left || right || up || down;
# 	}



