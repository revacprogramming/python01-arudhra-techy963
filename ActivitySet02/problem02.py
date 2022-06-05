

def input2no():
  a,b = int(input("input? "))
  return a,b

def add(a, b ):
  c = a + b
  return c

def output(a, b, sum):
  print(a,"+",b," is ",sum)


def main():
  a, b = input2no()
  sum = add(a, b)
  output(a, b, sum )

#if __name__ == '__main__':
main()
