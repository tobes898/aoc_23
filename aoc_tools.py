import os
from aocd import get_data
def setup():
    os.environ['AOC_SESSION'] = open("session_id.txt").readline().strip()

def load_test_input() -> list:
    res = []
    for line in open("test_input.txt"):
        res.append(line.strip())
    return res 

def load_input(day, year) -> list:
    return get_data(day=day, year=year).split('\n')


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str ) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def serach(self, word: str) -> bool:

        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            
            curr = curr.children[c]
        return curr.endOfWord
    

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True