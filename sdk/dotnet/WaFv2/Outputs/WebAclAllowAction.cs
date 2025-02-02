// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    /// <summary>
    /// Allow traffic towards application.
    /// </summary>
    [OutputType]
    public sealed class WebAclAllowAction
    {
        public readonly Outputs.WebAclCustomRequestHandling? CustomRequestHandling;

        [OutputConstructor]
        private WebAclAllowAction(Outputs.WebAclCustomRequestHandling? customRequestHandling)
        {
            CustomRequestHandling = customRequestHandling;
        }
    }
}
