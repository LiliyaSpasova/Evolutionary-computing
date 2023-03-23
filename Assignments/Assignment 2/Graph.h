#include <vector>
#include <fstream>
#include <cstring>
using namespace std;
struct Vertex
{
	int id;
	vector<int>  neighbours;
	int x;
	int y;
};

class Graph 
{
	public:
	vector<Vertex> vertices;
	void serealize();
};