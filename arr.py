def main():
  scores=[76,82,85,72,92]
  Total=sum(scores)
  average=Total/len(scores)
  print("===main/master branch output===")
  print(f"Scores:{scores}")
  print(f"Sum:{Total}")
  print(f"Average:{average}")
  print("===local branch output===")
  print(f"Maximum:{max(scores)}")
  print(f"Minimum:{min(scores)}")
if __name__=="__main__":
  main()
  
