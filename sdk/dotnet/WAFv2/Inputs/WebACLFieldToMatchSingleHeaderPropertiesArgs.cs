// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    public sealed class WebACLFieldToMatchSingleHeaderPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public WebACLFieldToMatchSingleHeaderPropertiesArgs()
        {
        }
        public static new WebACLFieldToMatchSingleHeaderPropertiesArgs Empty => new WebACLFieldToMatchSingleHeaderPropertiesArgs();
    }
}
