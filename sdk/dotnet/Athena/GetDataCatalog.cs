// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Athena
{
    public static class GetDataCatalog
    {
        /// <summary>
        /// Resource schema for AWS::Athena::DataCatalog
        /// </summary>
        public static Task<GetDataCatalogResult> InvokeAsync(GetDataCatalogArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDataCatalogResult>("aws-native:athena:getDataCatalog", args ?? new GetDataCatalogArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::Athena::DataCatalog
        /// </summary>
        public static Output<GetDataCatalogResult> Invoke(GetDataCatalogInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDataCatalogResult>("aws-native:athena:getDataCatalog", args ?? new GetDataCatalogInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDataCatalogArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters. 
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetDataCatalogArgs()
        {
        }
        public static new GetDataCatalogArgs Empty => new GetDataCatalogArgs();
    }

    public sealed class GetDataCatalogInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the data catalog to create. The catalog name must be unique for the AWS account and can use a maximum of 128 alphanumeric, underscore, at sign, or hyphen characters. 
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetDataCatalogInvokeArgs()
        {
        }
        public static new GetDataCatalogInvokeArgs Empty => new GetDataCatalogInvokeArgs();
    }


    [OutputType]
    public sealed class GetDataCatalogResult
    {
        /// <summary>
        /// A description of the data catalog to be created. 
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type. 
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Parameters;
        /// <summary>
        /// A list of comma separated tags to add to the data catalog that is created. 
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        /// <summary>
        /// The type of data catalog to create: LAMBDA for a federated catalog, GLUE for AWS Glue Catalog, or HIVE for an external hive metastore. 
        /// </summary>
        public readonly Pulumi.AwsNative.Athena.DataCatalogType? Type;

        [OutputConstructor]
        private GetDataCatalogResult(
            string? description,

            ImmutableDictionary<string, string>? parameters,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            Pulumi.AwsNative.Athena.DataCatalogType? type)
        {
            Description = description;
            Parameters = parameters;
            Tags = tags;
            Type = type;
        }
    }
}
