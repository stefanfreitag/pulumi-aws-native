// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2
{
    public static class GetStage
    {
        /// <summary>
        /// Resource Type definition for AWS::ApiGatewayV2::Stage
        /// </summary>
        public static Task<GetStageResult> InvokeAsync(GetStageArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetStageResult>("aws-native:apigatewayv2:getStage", args ?? new GetStageArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ApiGatewayV2::Stage
        /// </summary>
        public static Output<GetStageResult> Invoke(GetStageInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetStageResult>("aws-native:apigatewayv2:getStage", args ?? new GetStageInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStageArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetStageArgs()
        {
        }
        public static new GetStageArgs Empty => new GetStageArgs();
    }

    public sealed class GetStageInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetStageInvokeArgs()
        {
        }
        public static new GetStageInvokeArgs Empty => new GetStageInvokeArgs();
    }


    [OutputType]
    public sealed class GetStageResult
    {
        public readonly Outputs.StageAccessLogSettings? AccessLogSettings;
        public readonly string? AccessPolicyId;
        public readonly bool? AutoDeploy;
        public readonly string? ClientCertificateId;
        public readonly Outputs.StageRouteSettings? DefaultRouteSettings;
        public readonly string? DeploymentId;
        public readonly string? Description;
        public readonly string? Id;
        public readonly object? RouteSettings;
        public readonly object? StageVariables;
        public readonly object? Tags;

        [OutputConstructor]
        private GetStageResult(
            Outputs.StageAccessLogSettings? accessLogSettings,

            string? accessPolicyId,

            bool? autoDeploy,

            string? clientCertificateId,

            Outputs.StageRouteSettings? defaultRouteSettings,

            string? deploymentId,

            string? description,

            string? id,

            object? routeSettings,

            object? stageVariables,

            object? tags)
        {
            AccessLogSettings = accessLogSettings;
            AccessPolicyId = accessPolicyId;
            AutoDeploy = autoDeploy;
            ClientCertificateId = clientCertificateId;
            DefaultRouteSettings = defaultRouteSettings;
            DeploymentId = deploymentId;
            Description = description;
            Id = id;
            RouteSettings = routeSettings;
            StageVariables = stageVariables;
            Tags = tags;
        }
    }
}
