import math

class ObjectTracker:
    def __init__(self):
        # Dictionary to store object positions
        self.center_points = {}

        # Unique object ID 
        self.id_count = 0

        # Store  abandoned
        self.abandoned_temp = {}

    def update(self, objects_rect):

        objects_bbs_ids = []
        abandoned_objects = []

        # Get center point of new objects
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + w // 2)  # Center X
            cy = (y + h // 2)  # Center Y

            same_object_detected = False

            # Compare with existing objects 
            for obj_id, prev_center in self.center_points.items():
                distance = math.hypot(cx - prev_center[0], cy - prev_center[1])

                # If the object is near a previous one, update its position
                if distance < 25:
                    self.center_points[obj_id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, obj_id, distance])
                    same_object_detected = True

                    # Check if the object is stationary 
                    if obj_id in self.abandoned_temp:
                        if distance < 1:  # Object hasn't moved
                            if self.abandoned_temp[obj_id] > 100:  # Threshold for abandoned detection
                                abandoned_objects.append([obj_id, x, y, w, h, distance])
                            else:
                                self.abandoned_temp[obj_id] += 1  # Increase stationary count
                    break

            # If new object detected, assign a new ID
            if not same_object_detected:
                self.center_points[self.id_count] = (cx, cy)
                self.abandoned_temp[self.id_count] = 1  # Start count for abandonment check
                objects_bbs_ids.append([x, y, w, h, self.id_count, None])
                self.id_count += 1

        # Remove old objects that are no longer detected
        new_center_points = {}
        abandoned_temp_updated = {}

        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, obj_id, _ = obj_bb_id
            new_center_points[obj_id] = self.center_points[obj_id]

            if obj_id in self.abandoned_temp:
                abandoned_temp_updated[obj_id] = self.abandoned_temp[obj_id]

        self.center_points = new_center_points.copy()
        self.abandoned_temp = abandoned_temp_updated.copy()

        return objects_bbs_ids, abandoned_objects



