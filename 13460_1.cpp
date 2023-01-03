#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {

    // input
    int n, m;
    cin >> n >> m;

    char board[10][10];
    pair<int, int> blue, red, hole;

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; i++) {

            cin >> board[i][j];

            if(board[i][j] == 'B')
                blue = make_pair(i, j);
            
            else if(board[i][j] == 'R')
                red = make_pair(i, j);
            
            else if(board[i][j] == 'O')
                hole = make_pair(i, j);
        }

    // Up, Down, Left, Right, integer
    vector<char> stack;

    int ans = INT_MAX;

    int move = 0;
    vector<pair<int, int>> location_red;
    vector<pair<int, int>> location_blue;
    do {
        location_red.push_back(red);
        location_blue.push_back(blue);
        stack.push_back(move++ + '0');

        // check possible way
        if(board[red.first - 1][red.second] == '.')
            stack.push_back('u');
        
        else if(board[red.first][red.second + 1] == '.')
            stack.push_back('r');
        
        else if(board[red.first + 1][red.second] == '.')
            stack.push_back('d');
        
        else if(board[red.first][red.second - 1] == '.')
            stack.push_back('l');

        while(true) {
            if('0' <= stack.back() && stack.back() <= '9') {
                move--;
                stack.pop_back();
                location_red.pop_back();
                location_blue.pop_back();
            }

            // move
            else if(stack.back() == 'u') {
                stack.pop_back();

                int red_i = red.first;
                int red_j = red.second;
                int blue_i = blue.first;
                int blue_j = blue.second;

                if(red_i > blue_i) {
                    board[red_i][red_j] = '.';
                    while(board[red_i][red_j] == '.')
                        red_i--;
                    
                    if(board[red_i][red_j] == 'O') {
                        ans = move < ans ? move : ans;
                        
                        while('0' > stack.back() || stack.back() > '9')
                            stack.pop_back();
                        stack.pop_back();

                        location_red.pop_back();
                        location_blue.pop_back();

                        board[location_red.back().first][location_red.back().second] = 'R';
                        board[location_blue.back().first][location_blue.back().second] = 'B';
                    }

                    else {
                        red_i++;
                        board[red_i][red_j] = 'R';

                        board[blue_i][blue_j] = '.';
                        while(board[blue_i][blue_j] == '.')
                            blue_i--;

                        blue_i++;
                        board[blue_i][blue_j] = 'B';
                    }
                }
            }
        }
    } while(move != 0);
}