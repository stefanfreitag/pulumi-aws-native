// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateTableFieldCustomIconContentArgs : global::Pulumi.ResourceArgs
    {
        [Input("icon")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateTableFieldIconSetType>? Icon { get; set; }

        public TemplateTableFieldCustomIconContentArgs()
        {
        }
        public static new TemplateTableFieldCustomIconContentArgs Empty => new TemplateTableFieldCustomIconContentArgs();
    }
}
