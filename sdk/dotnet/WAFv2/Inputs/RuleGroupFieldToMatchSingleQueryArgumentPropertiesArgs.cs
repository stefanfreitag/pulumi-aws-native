// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    /// <summary>
    /// One query argument in a web request, identified by name, for example UserName or SalesRegion. The name can be up to 30 characters long and isn't case sensitive.
    /// </summary>
    public sealed class RuleGroupFieldToMatchSingleQueryArgumentPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public RuleGroupFieldToMatchSingleQueryArgumentPropertiesArgs()
        {
        }
        public static new RuleGroupFieldToMatchSingleQueryArgumentPropertiesArgs Empty => new RuleGroupFieldToMatchSingleQueryArgumentPropertiesArgs();
    }
}
