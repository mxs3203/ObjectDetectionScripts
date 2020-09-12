import image_bbox_slicer as ibs

im_src = 'JPEGImages/'
an_src = 'Annotations'
im_dst = 'JPEGImages_new'
an_dst = 'Annotations_new'

slicer = ibs.Slicer()
slicer.config_dirs(img_src=im_src, ann_src=an_src, 
                   img_dst=im_dst, ann_dst=an_dst)

slicer.keep_partial_labels = False
slicer.save_before_after_map = True

#slicer.slice_by_number(number_tiles=4)
#slicer.visualize_sliced_random()
slicer.slice_by_size(tile_size=(500,500), tile_overlap=0)
slicer.visualize_sliced_random()
