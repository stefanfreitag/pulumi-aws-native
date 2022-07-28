// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Redshift
{
    public static class GetClusterSecurityGroupIngress
    {
        /// <summary>
        /// Resource Type definition for AWS::Redshift::ClusterSecurityGroupIngress
        /// </summary>
        public static Task<GetClusterSecurityGroupIngressResult> InvokeAsync(GetClusterSecurityGroupIngressArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClusterSecurityGroupIngressResult>("aws-native:redshift:getClusterSecurityGroupIngress", args ?? new GetClusterSecurityGroupIngressArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Redshift::ClusterSecurityGroupIngress
        /// </summary>
        public static Output<GetClusterSecurityGroupIngressResult> Invoke(GetClusterSecurityGroupIngressInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetClusterSecurityGroupIngressResult>("aws-native:redshift:getClusterSecurityGroupIngress", args ?? new GetClusterSecurityGroupIngressInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClusterSecurityGroupIngressArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetClusterSecurityGroupIngressArgs()
        {
        }
        public static new GetClusterSecurityGroupIngressArgs Empty => new GetClusterSecurityGroupIngressArgs();
    }

    public sealed class GetClusterSecurityGroupIngressInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetClusterSecurityGroupIngressInvokeArgs()
        {
        }
        public static new GetClusterSecurityGroupIngressInvokeArgs Empty => new GetClusterSecurityGroupIngressInvokeArgs();
    }


    [OutputType]
    public sealed class GetClusterSecurityGroupIngressResult
    {
        public readonly string? Id;

        [OutputConstructor]
        private GetClusterSecurityGroupIngressResult(string? id)
        {
            Id = id;
        }
    }
}
