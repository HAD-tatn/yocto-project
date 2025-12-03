class TimeColorDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        # Chỉ áp dụng cho cột Time (cột 3)
        if index.column() == 3:
            option.backgroundBrush = QBrush(QColor("#9707b8"))   # màu nền Time
        super().paint(painter, option, index)