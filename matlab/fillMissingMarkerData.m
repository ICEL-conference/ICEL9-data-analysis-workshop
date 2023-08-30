function [cleanedData,missingIndices,Cleaned_Tag] = fillMissingMarkerData(dataToClean,MaxGap,plotResults_Question)


if mean(isnan(dataToClean)) > 0
    [cleanedData,missingIndices] = fillmissing(dataToClean,"pchip","MaxGap",MaxGap);
    Cleaned_Tag = 'Yes';
else
    cleanedData = dataToClean;
    missingIndices = NaN;
    Cleaned_Tag = 'No';
end

if plotResults_Question
    % Display results
    figure

    % Plot cleaned data
    plot(dataToClean,"Color",[0 114 189]/255,"LineWidth",1.5,...
        "DisplayName","Cleaned data")
    hold on
    if ~isnan(missingIndices)
        % Plot filled missing entries
        plot(find(missingIndices),cleanedData(missingIndices),".","MarkerSize",12,...
            "Color",[217 83 25]/255,"DisplayName","Filled missing entries")
        title("Number of filled missing entries: " + nnz(missingIndices))
    
        hold off
        legend
    end
end
end