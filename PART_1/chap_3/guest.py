# guest list
guest= ['alex', 'william', 'robin']
print (guest)
message= "You guys are invited to dinner."
print (guest[0].title(), guest[1].title(), guest[2].title() , message)
del guest[1]
print (guest)
guest.append('harry')
message= "William couldn't make it so I invited Harry instead."
print (message)
message = " I just found a bigger table so thinking of adding 3 more guests"
print (message)
guest.insert(0,'Louis')
guest.insert(-1, 'Liam')
guest.append('Niall')
print (f"The new guest list are " ,guest)

# shrinking guest list
message=" I just found out that your new dinner table won’t arrive in time for the dinner, and I have space for only two guests. I'm extremely sorry!"
guest_1= guest.pop()
guest_2= guest.pop()
guest_3= guest.pop()
guest_4= guest.pop()
print(guest[0], "You're invited")
print(guest[1], "You're invited")
print(guest)
del guest[0]
del guest[0]
print(guest)


# dinner guests
print(len(guest))