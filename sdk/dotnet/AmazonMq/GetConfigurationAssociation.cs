// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AmazonMq
{
    public static class GetConfigurationAssociation
    {
        /// <summary>
        /// Resource Type definition for AWS::AmazonMQ::ConfigurationAssociation
        /// </summary>
        public static Task<GetConfigurationAssociationResult> InvokeAsync(GetConfigurationAssociationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetConfigurationAssociationResult>("aws-native:amazonmq:getConfigurationAssociation", args ?? new GetConfigurationAssociationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AmazonMQ::ConfigurationAssociation
        /// </summary>
        public static Output<GetConfigurationAssociationResult> Invoke(GetConfigurationAssociationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetConfigurationAssociationResult>("aws-native:amazonmq:getConfigurationAssociation", args ?? new GetConfigurationAssociationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetConfigurationAssociationArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetConfigurationAssociationArgs()
        {
        }
        public static new GetConfigurationAssociationArgs Empty => new GetConfigurationAssociationArgs();
    }

    public sealed class GetConfigurationAssociationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetConfigurationAssociationInvokeArgs()
        {
        }
        public static new GetConfigurationAssociationInvokeArgs Empty => new GetConfigurationAssociationInvokeArgs();
    }


    [OutputType]
    public sealed class GetConfigurationAssociationResult
    {
        public readonly Outputs.ConfigurationAssociationConfigurationId? Configuration;
        public readonly string? Id;

        [OutputConstructor]
        private GetConfigurationAssociationResult(
            Outputs.ConfigurationAssociationConfigurationId? configuration,

            string? id)
        {
            Configuration = configuration;
            Id = id;
        }
    }
}
