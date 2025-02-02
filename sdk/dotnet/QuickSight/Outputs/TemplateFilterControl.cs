// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplateFilterControl
    {
        public readonly Outputs.TemplateFilterDateTimePickerControl? DateTimePicker;
        public readonly Outputs.TemplateFilterDropDownControl? Dropdown;
        public readonly Outputs.TemplateFilterListControl? List;
        public readonly Outputs.TemplateFilterRelativeDateTimeControl? RelativeDateTime;
        public readonly Outputs.TemplateFilterSliderControl? Slider;
        public readonly Outputs.TemplateFilterTextAreaControl? TextArea;
        public readonly Outputs.TemplateFilterTextFieldControl? TextField;

        [OutputConstructor]
        private TemplateFilterControl(
            Outputs.TemplateFilterDateTimePickerControl? dateTimePicker,

            Outputs.TemplateFilterDropDownControl? dropdown,

            Outputs.TemplateFilterListControl? list,

            Outputs.TemplateFilterRelativeDateTimeControl? relativeDateTime,

            Outputs.TemplateFilterSliderControl? slider,

            Outputs.TemplateFilterTextAreaControl? textArea,

            Outputs.TemplateFilterTextFieldControl? textField)
        {
            DateTimePicker = dateTimePicker;
            Dropdown = dropdown;
            List = list;
            RelativeDateTime = relativeDateTime;
            Slider = slider;
            TextArea = textArea;
            TextField = textField;
        }
    }
}
