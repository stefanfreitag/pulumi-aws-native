// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFRegional
{
    public static class GetWebACLAssociation
    {
        /// <summary>
        /// Resource Type definition for AWS::WAFRegional::WebACLAssociation
        /// </summary>
        public static Task<GetWebACLAssociationResult> InvokeAsync(GetWebACLAssociationArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetWebACLAssociationResult>("aws-native:wafregional:getWebACLAssociation", args ?? new GetWebACLAssociationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::WAFRegional::WebACLAssociation
        /// </summary>
        public static Output<GetWebACLAssociationResult> Invoke(GetWebACLAssociationInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetWebACLAssociationResult>("aws-native:wafregional:getWebACLAssociation", args ?? new GetWebACLAssociationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetWebACLAssociationArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetWebACLAssociationArgs()
        {
        }
        public static new GetWebACLAssociationArgs Empty => new GetWebACLAssociationArgs();
    }

    public sealed class GetWebACLAssociationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetWebACLAssociationInvokeArgs()
        {
        }
        public static new GetWebACLAssociationInvokeArgs Empty => new GetWebACLAssociationInvokeArgs();
    }


    [OutputType]
    public sealed class GetWebACLAssociationResult
    {
        public readonly string? Id;

        [OutputConstructor]
        private GetWebACLAssociationResult(string? id)
        {
            Id = id;
        }
    }
}
