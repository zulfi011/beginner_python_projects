with open('story.txt','r') as f:
    story = f.read()

start_tar = "<"
end_tar = ">"
start_idx = -1
words = set()

for idx,ele in enumerate(story):
    if ele == start_tar:
        start_idx = idx
    if ele == end_tar and start_idx != -1:
        word = story[start_idx:idx+1]
        words.add(word)
        start_idx = -1

ans = {}
for word in words:
    line = input(word[1:-1]+" : ")
    ans[word] = line

for key,val in ans.items():
    story = story.replace(key,val)

print("\n",story)