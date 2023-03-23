#include <iostream>
#include <fstream>
#include <cstring>
#include <filesystem>
#include "DoublyLinkedList.h"
#include "Graph.h"

using namespace std;
int main()
{
    std::filesystem::path path{ "C:\\TestingFolder" }; //creates TestingFolder object on C:
    path /= "my new file.txt"; //put something into there
    std::filesystem::create_directories(path.parent_path()); //add directories based on the object path (without this line it will not work)

    std::ofstream ofs(path);
    ofs << "this is some text in the new file\n"; 
    ofs.close();
}