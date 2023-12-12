import matplotlib.pyplot as plt
def main():
    data =[[2,10], [2,5], [8,4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]]
    n = 0
    k = 3
    centroids = [data[i] for i in range(k)]
    flag = True
    while flag:
        n += 1
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [((point[0] - c[0])**2 + (point[1] - c[1])**2) ** 0.5 for c in centroids]
            cluster_assignment = distances.index(min(distances))
            clusters[cluster_assignment].append(point)
        new_centroids = [(
            sum(point[0] for point in cluster) / max(1, len(cluster)),
            sum(point[1] for point in cluster) / max(1, len(cluster))
        ) for cluster in clusters]
        if centroids == new_centroids:
            flag = False
        else:
            centroids = new_centroids
    print("\nFinal Clusters: ")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}:")
        for point in cluster:
            print(point)
    colors = ['r', 'g', 'b', 'y']
    for i, cluster in enumerate(clusters):
        x_values = [point[0] for point in cluster]
        y_values = [point[1] for point in cluster]
        plt.scatter(x_values, y_values, c=colors[i], label=f'Cluster{i + 1}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()