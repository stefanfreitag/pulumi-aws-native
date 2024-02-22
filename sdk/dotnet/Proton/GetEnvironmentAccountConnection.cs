// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Proton
{
    public static class GetEnvironmentAccountConnection
    {
        /// <summary>
        /// Resource Schema describing various properties for AWS Proton Environment Account Connections resources.
        /// </summary>
        public static Task<GetEnvironmentAccountConnectionResult> InvokeAsync(GetEnvironmentAccountConnectionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEnvironmentAccountConnectionResult>("aws-native:proton:getEnvironmentAccountConnection", args ?? new GetEnvironmentAccountConnectionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Schema describing various properties for AWS Proton Environment Account Connections resources.
        /// </summary>
        public static Output<GetEnvironmentAccountConnectionResult> Invoke(GetEnvironmentAccountConnectionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEnvironmentAccountConnectionResult>("aws-native:proton:getEnvironmentAccountConnection", args ?? new GetEnvironmentAccountConnectionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEnvironmentAccountConnectionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the environment account connection.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetEnvironmentAccountConnectionArgs()
        {
        }
        public static new GetEnvironmentAccountConnectionArgs Empty => new GetEnvironmentAccountConnectionArgs();
    }

    public sealed class GetEnvironmentAccountConnectionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the environment account connection.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetEnvironmentAccountConnectionInvokeArgs()
        {
        }
        public static new GetEnvironmentAccountConnectionInvokeArgs Empty => new GetEnvironmentAccountConnectionInvokeArgs();
    }


    [OutputType]
    public sealed class GetEnvironmentAccountConnectionResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the environment account connection.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.
        /// </summary>
        public readonly string? CodebuildRoleArn;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account.
        /// </summary>
        public readonly string? ComponentRoleArn;
        /// <summary>
        /// The environment account that's connected to the environment account connection.
        /// </summary>
        public readonly string? EnvironmentAccountId;
        /// <summary>
        /// The name of the AWS Proton environment that's created in the associated management account.
        /// </summary>
        public readonly string? EnvironmentName;
        /// <summary>
        /// The ID of the environment account connection.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The ID of the management account that accepts or rejects the environment account connection. You create an manage the AWS Proton environment in this account. If the management account accepts the environment account connection, AWS Proton can use the associated IAM role to provision environment infrastructure resources in the associated environment account.
        /// </summary>
        public readonly string? ManagementAccountId;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the IAM service role that's created in the environment account. AWS Proton uses this role to provision infrastructure resources in the associated environment account.
        /// </summary>
        public readonly string? RoleArn;
        /// <summary>
        /// The status of the environment account connection.
        /// </summary>
        public readonly Pulumi.AwsNative.Proton.EnvironmentAccountConnectionStatus? Status;
        /// <summary>
        /// &lt;p&gt;An optional list of metadata items that you can associate with the Proton environment account connection. A tag is a key-value pair.&lt;/p&gt;
        ///          &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/proton/latest/userguide/resources.html"&gt;Proton resources and tagging&lt;/a&gt; in the
        ///         &lt;i&gt;Proton User Guide&lt;/i&gt;.&lt;/p&gt;
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetEnvironmentAccountConnectionResult(
            string? arn,

            string? codebuildRoleArn,

            string? componentRoleArn,

            string? environmentAccountId,

            string? environmentName,

            string? id,

            string? managementAccountId,

            string? roleArn,

            Pulumi.AwsNative.Proton.EnvironmentAccountConnectionStatus? status,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Arn = arn;
            CodebuildRoleArn = codebuildRoleArn;
            ComponentRoleArn = componentRoleArn;
            EnvironmentAccountId = environmentAccountId;
            EnvironmentName = environmentName;
            Id = id;
            ManagementAccountId = managementAccountId;
            RoleArn = roleArn;
            Status = status;
            Tags = tags;
        }
    }
}
