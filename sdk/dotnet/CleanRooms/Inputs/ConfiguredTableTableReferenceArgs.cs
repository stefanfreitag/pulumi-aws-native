// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms.Inputs
{

    public sealed class ConfiguredTableTableReferenceArgs : global::Pulumi.ResourceArgs
    {
        [Input("glue", required: true)]
        public Input<Inputs.ConfiguredTableGlueTableReferenceArgs> Glue { get; set; } = null!;

        public ConfiguredTableTableReferenceArgs()
        {
        }
        public static new ConfiguredTableTableReferenceArgs Empty => new ConfiguredTableTableReferenceArgs();
    }
}
