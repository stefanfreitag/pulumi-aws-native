// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTTwinMaker
{
    public static class GetComponentType
    {
        /// <summary>
        /// Resource schema for AWS::IoTTwinMaker::ComponentType
        /// </summary>
        public static Task<GetComponentTypeResult> InvokeAsync(GetComponentTypeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetComponentTypeResult>("aws-native:iottwinmaker:getComponentType", args ?? new GetComponentTypeArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::IoTTwinMaker::ComponentType
        /// </summary>
        public static Output<GetComponentTypeResult> Invoke(GetComponentTypeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetComponentTypeResult>("aws-native:iottwinmaker:getComponentType", args ?? new GetComponentTypeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetComponentTypeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the component type.
        /// </summary>
        [Input("componentTypeId", required: true)]
        public string ComponentTypeId { get; set; } = null!;

        /// <summary>
        /// The ID of the workspace that contains the component type.
        /// </summary>
        [Input("workspaceId", required: true)]
        public string WorkspaceId { get; set; } = null!;

        public GetComponentTypeArgs()
        {
        }
        public static new GetComponentTypeArgs Empty => new GetComponentTypeArgs();
    }

    public sealed class GetComponentTypeInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the component type.
        /// </summary>
        [Input("componentTypeId", required: true)]
        public Input<string> ComponentTypeId { get; set; } = null!;

        /// <summary>
        /// The ID of the workspace that contains the component type.
        /// </summary>
        [Input("workspaceId", required: true)]
        public Input<string> WorkspaceId { get; set; } = null!;

        public GetComponentTypeInvokeArgs()
        {
        }
        public static new GetComponentTypeInvokeArgs Empty => new GetComponentTypeInvokeArgs();
    }


    [OutputType]
    public sealed class GetComponentTypeResult
    {
        /// <summary>
        /// The ARN of the component type.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// An map of the composite component types in the component type. Each composite component type's key must be unique to this map.
        /// </summary>
        public readonly object? CompositeComponentTypes;
        /// <summary>
        /// The date and time when the component type was created.
        /// </summary>
        public readonly string? CreationDateTime;
        /// <summary>
        /// The description of the component type.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Specifies the parent component type to extend.
        /// </summary>
        public readonly ImmutableArray<string> ExtendsFrom;
        /// <summary>
        /// a Map of functions in the component type. Each function's key must be unique to this map.
        /// </summary>
        public readonly object? Functions;
        /// <summary>
        /// A Boolean value that specifies whether the component type is abstract.
        /// </summary>
        public readonly bool? IsAbstract;
        /// <summary>
        /// A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.
        /// </summary>
        public readonly bool? IsSchemaInitialized;
        /// <summary>
        /// A Boolean value that specifies whether an entity can have more than one component of this type.
        /// </summary>
        public readonly bool? IsSingleton;
        /// <summary>
        /// An map of the property definitions in the component type. Each property definition's key must be unique to this map.
        /// </summary>
        public readonly object? PropertyDefinitions;
        /// <summary>
        /// An map of the property groups in the component type. Each property group's key must be unique to this map.
        /// </summary>
        public readonly object? PropertyGroups;
        /// <summary>
        /// The current status of the component type.
        /// </summary>
        public readonly Outputs.ComponentTypeStatus? Status;
        /// <summary>
        /// A map of key-value pairs to associate with a resource.
        /// </summary>
        public readonly object? Tags;
        /// <summary>
        /// The last date and time when the component type was updated.
        /// </summary>
        public readonly string? UpdateDateTime;

        [OutputConstructor]
        private GetComponentTypeResult(
            string? arn,

            object? compositeComponentTypes,

            string? creationDateTime,

            string? description,

            ImmutableArray<string> extendsFrom,

            object? functions,

            bool? isAbstract,

            bool? isSchemaInitialized,

            bool? isSingleton,

            object? propertyDefinitions,

            object? propertyGroups,

            Outputs.ComponentTypeStatus? status,

            object? tags,

            string? updateDateTime)
        {
            Arn = arn;
            CompositeComponentTypes = compositeComponentTypes;
            CreationDateTime = creationDateTime;
            Description = description;
            ExtendsFrom = extendsFrom;
            Functions = functions;
            IsAbstract = isAbstract;
            IsSchemaInitialized = isSchemaInitialized;
            IsSingleton = isSingleton;
            PropertyDefinitions = propertyDefinitions;
            PropertyGroups = propertyGroups;
            Status = status;
            Tags = tags;
            UpdateDateTime = updateDateTime;
        }
    }
}
