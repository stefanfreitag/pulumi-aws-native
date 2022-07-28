// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync
{
    public static class GetGraphQLSchema
    {
        /// <summary>
        /// Resource Type definition for AWS::AppSync::GraphQLSchema
        /// </summary>
        public static Task<GetGraphQLSchemaResult> InvokeAsync(GetGraphQLSchemaArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetGraphQLSchemaResult>("aws-native:appsync:getGraphQLSchema", args ?? new GetGraphQLSchemaArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AppSync::GraphQLSchema
        /// </summary>
        public static Output<GetGraphQLSchemaResult> Invoke(GetGraphQLSchemaInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetGraphQLSchemaResult>("aws-native:appsync:getGraphQLSchema", args ?? new GetGraphQLSchemaInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetGraphQLSchemaArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetGraphQLSchemaArgs()
        {
        }
        public static new GetGraphQLSchemaArgs Empty => new GetGraphQLSchemaArgs();
    }

    public sealed class GetGraphQLSchemaInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetGraphQLSchemaInvokeArgs()
        {
        }
        public static new GetGraphQLSchemaInvokeArgs Empty => new GetGraphQLSchemaInvokeArgs();
    }


    [OutputType]
    public sealed class GetGraphQLSchemaResult
    {
        public readonly string? Definition;
        public readonly string? DefinitionS3Location;
        public readonly string? Id;

        [OutputConstructor]
        private GetGraphQLSchemaResult(
            string? definition,

            string? definitionS3Location,

            string? id)
        {
            Definition = definition;
            DefinitionS3Location = definitionS3Location;
            Id = id;
        }
    }
}
