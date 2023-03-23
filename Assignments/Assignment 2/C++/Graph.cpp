#include "Graph.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

void Graph::serealize()
{
	string line;
	std::ifstream file("Assignment 2\\graphData.txt");
	bool isOpen=file.is_open();
	while (std::getline(file,line))
	{
		std::cout << line << std::endl;
		for (int i=0; i<line.length();i++)
		{
			int id;
			int x;
			int y;
			vector<int> neighbours;
			neighbours.push_back(2);
			//split
			Vertex v;
			v.id=id;
			v.x=x;
			v.y=y;
			v.neighbours=neighbours;
			this->vertices.push_back(v);
		}
	}
	for( std::string line; std::getline( file, line ); )
	{
		std::cout << line;
	}
	file.close(); 
}
