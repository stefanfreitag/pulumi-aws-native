// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateDecimalValueWhenUnsetConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("customValue")]
        public Input<double>? CustomValue { get; set; }

        [Input("valueWhenUnsetOption")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateValueWhenUnsetOption>? ValueWhenUnsetOption { get; set; }

        public TemplateDecimalValueWhenUnsetConfigurationArgs()
        {
        }
        public static new TemplateDecimalValueWhenUnsetConfigurationArgs Empty => new TemplateDecimalValueWhenUnsetConfigurationArgs();
    }
}
