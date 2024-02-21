// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecr
{
    public static class GetPublicRepository
    {
        /// <summary>
        /// The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR
        /// </summary>
        public static Task<GetPublicRepositoryResult> InvokeAsync(GetPublicRepositoryArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPublicRepositoryResult>("aws-native:ecr:getPublicRepository", args ?? new GetPublicRepositoryArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::ECR::PublicRepository resource specifies an Amazon Elastic Container Public Registry (Amazon Public ECR) repository, where users can push and pull Docker images. For more information, see https://docs.aws.amazon.com/AmazonECR
        /// </summary>
        public static Output<GetPublicRepositoryResult> Invoke(GetPublicRepositoryInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPublicRepositoryResult>("aws-native:ecr:getPublicRepository", args ?? new GetPublicRepositoryInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPublicRepositoryArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        /// </summary>
        [Input("repositoryName", required: true)]
        public string RepositoryName { get; set; } = null!;

        public GetPublicRepositoryArgs()
        {
        }
        public static new GetPublicRepositoryArgs Empty => new GetPublicRepositoryArgs();
    }

    public sealed class GetPublicRepositoryInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a/nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html.
        /// </summary>
        [Input("repositoryName", required: true)]
        public Input<string> RepositoryName { get; set; } = null!;

        public GetPublicRepositoryInvokeArgs()
        {
        }
        public static new GetPublicRepositoryInvokeArgs Empty => new GetPublicRepositoryInvokeArgs();
    }


    [OutputType]
    public sealed class GetPublicRepositoryResult
    {
        public readonly string? Arn;
        /// <summary>
        /// The CatalogData property type specifies Catalog data for ECR Public Repository. For information about Catalog Data, see &lt;link&gt;
        /// </summary>
        public readonly Outputs.RepositoryCatalogDataProperties? RepositoryCatalogData;
        /// <summary>
        /// The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. 
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ECR::PublicRepository` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? RepositoryPolicyText;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.PublicRepositoryTag> Tags;

        [OutputConstructor]
        private GetPublicRepositoryResult(
            string? arn,

            Outputs.RepositoryCatalogDataProperties? repositoryCatalogData,

            object? repositoryPolicyText,

            ImmutableArray<Outputs.PublicRepositoryTag> tags)
        {
            Arn = arn;
            RepositoryCatalogData = repositoryCatalogData;
            RepositoryPolicyText = repositoryPolicyText;
            Tags = tags;
        }
    }
}
