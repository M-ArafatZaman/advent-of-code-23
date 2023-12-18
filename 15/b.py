data = input().split(",")

def hsh(s) -> int:
    curr = 0
    for c in s:
        curr = (17*(curr + ord(c))) % 256
    return curr

def main():
    # linked lists 
    box = [{"head": None, "tail": None} for _ in range(256)]

    for d in data:
        label, focal = d.split("=") if "=" in d else d.split("-")
        box_i = hsh(label)
        
        if "=" in d:
            # Insert/update
            if label in box[box_i]:
                box[box_i][label]["value"] = focal
            else:
                box[box_i][label] = {
                    "value": focal,
                    "prev": None,
                    "next": None
                }
                if not box[box_i]["head"]:
                    box[box_i]["head"] = box[box_i][label]
                    box[box_i]["tail"] = box[box_i][label]
                else:
                    box[box_i][label]["prev"] = box[box_i]["tail"]
                    box[box_i]["tail"]["next"] = box[box_i][label]
                    box[box_i]["tail"] = box[box_i][label]

        else:
            # Remove
            if label in box[box_i]:
                if box[box_i][label]["prev"]:
                    box[box_i][label]["prev"]["next"] = box[box_i][label]["next"]
                else:
                    box[box_i]["head"] = box[box_i][label]["next"]
                if box[box_i][label]["next"]:
                    box[box_i][label]["next"]["prev"] = box[box_i][label]["prev"]
                else:
                    box[box_i]["tail"] = box[box_i][label]["prev"]
                del box[box_i][label]
    
    s = 0
    for i, b in enumerate(box):
        if b["head"]:
            p = 1
            curr = b["head"]
            s += (i+1) * p * int(curr["value"])
            while curr["next"]:
                curr = curr["next"]
                p += 1
                s += (i+1) * p * int(curr["value"])
    
    print(s)

if __name__ == "__main__":
    main()