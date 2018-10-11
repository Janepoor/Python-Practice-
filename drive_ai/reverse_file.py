# inplace reverse，分别头尾读出来一个4k块，分别reverse再swap，然后从mutex聊到崩溃恢复
# read(fileName, startIndex, buffer, bufferSize); write(fileName, startIndex, buffer, bufferSize);

# read(fileHandler，buffer, sz): 读文件中的内容到buffer里，sz要读取内容的size。
# write(fileHandler, buffer, start): 将buffer中的内容写入start开始的位置. 留学申请论坛-一亩三分地
# 让实现一个很大的文件逆序，文件的大小是已知的

# 1. read chunk by chunk, const int buffer_size=1024*1024;
# 2. use two pointers, one reads from begining, one reads from end, swap the two chunks
# 3. reverse the characters inside the chunks.

read(name,0, buffer, 4k)


left, right = 0, len(size)-1

while left < right:
    reverse(left_side)
    reverse(right_side)
    swap(left_side, right_side)
