// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateColumnSchemaArgs : global::Pulumi.ResourceArgs
    {
        [Input("dataType")]
        public Input<string>? DataType { get; set; }

        [Input("geographicRole")]
        public Input<string>? GeographicRole { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public TemplateColumnSchemaArgs()
        {
        }
        public static new TemplateColumnSchemaArgs Empty => new TemplateColumnSchemaArgs();
    }
}
