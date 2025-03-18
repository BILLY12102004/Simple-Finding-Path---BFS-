from collections import deque

def bfs_shortest_route(city_map, start, goal):
    if start not in city_map or goal not in city_map:
        return f"Tempat '{start}' atau '{goal}' tidak ditemukan dalam peta."

    queue = deque([[start]])  # Antrian BFS berisi jalur yang sedang ditelusuri
    visited = set()  # Menyimpan tempat yang sudah dikunjungi

    while queue:
        path = queue.popleft()  # Ambil jalur pertama dari antrian
        node = path[-1]  # Ambil tempat terakhir dalam jalur

        if node == goal:
            return path  # Jika sudah sampai tujuan, kembalikan jalurnya
        
        if node not in visited:
            visited.add(node)
            for neighbor in city_map[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return f"Tidak ada rute dari '{start}' ke '{goal}'."

# Struktur peta kota
city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

# Contoh penggunaan
start_location = "Home"
end_location = "Hospital"
result = bfs_shortest_route(city_map, start_location, end_location)
print("Jalur Terpendek:", result)