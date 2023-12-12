import matplotlib.pyplot as plt

def main():
    data = [[10, 2], [4, 6], [2, 8], [12, 10], [3, 5], [20, 18], [30, 25], [11, 8], [25, 30], [31, 28]]  # 2D data
    k = 2  # Number of clusters
    centroids = [data[i] for i in range(k)]  # Initialize centroids with the first k data points

    flag = True
    n = 0

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

        if new_centroids == centroids:
            flag = False
        else:
            centroids = new_centroids

    print("\nFinal clusters:")
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i + 1}:")
        for point in cluster:
            print(point)

    # Plot the clusters
    colors = ['r', 'b', 'g', 'c', 'm', 'y']
    for i, cluster in enumerate(clusters):
        x_values = [point[0] for point in cluster]
        y_values = [point[1] for point in cluster]
        plt.scatter(x_values, y_values, c=colors[i], label=f'Cluster {i + 1}')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
