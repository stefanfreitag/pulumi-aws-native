// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CodePipeline::Pipeline
 *
 * @deprecated Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Pipeline extends pulumi.CustomResource {
    /**
     * Get an existing Pipeline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Pipeline {
        pulumi.log.warn("Pipeline is deprecated: Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Pipeline(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:codepipeline:Pipeline';

    /**
     * Returns true if the given object is an instance of Pipeline.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Pipeline {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Pipeline.__pulumiType;
    }

    public readonly artifactStore!: pulumi.Output<outputs.codepipeline.PipelineArtifactStore | undefined>;
    public readonly artifactStores!: pulumi.Output<outputs.codepipeline.PipelineArtifactStoreMap[] | undefined>;
    public readonly disableInboundStageTransitions!: pulumi.Output<outputs.codepipeline.PipelineStageTransition[] | undefined>;
    public readonly executionMode!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly pipelineType!: pulumi.Output<string | undefined>;
    public readonly restartExecutionOnUpdate!: pulumi.Output<boolean | undefined>;
    public readonly roleArn!: pulumi.Output<string>;
    public readonly stages!: pulumi.Output<outputs.codepipeline.PipelineStageDeclaration[]>;
    public readonly tags!: pulumi.Output<outputs.codepipeline.PipelineTag[] | undefined>;
    public readonly triggers!: pulumi.Output<outputs.codepipeline.PipelineTriggerDeclaration[] | undefined>;
    public readonly variables!: pulumi.Output<outputs.codepipeline.PipelineVariableDeclaration[] | undefined>;
    public /*out*/ readonly version!: pulumi.Output<string>;

    /**
     * Create a Pipeline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: PipelineArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Pipeline is deprecated: Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.roleArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'roleArn'");
            }
            if ((!args || args.stages === undefined) && !opts.urn) {
                throw new Error("Missing required property 'stages'");
            }
            resourceInputs["artifactStore"] = args ? args.artifactStore : undefined;
            resourceInputs["artifactStores"] = args ? args.artifactStores : undefined;
            resourceInputs["disableInboundStageTransitions"] = args ? args.disableInboundStageTransitions : undefined;
            resourceInputs["executionMode"] = args ? args.executionMode : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["pipelineType"] = args ? args.pipelineType : undefined;
            resourceInputs["restartExecutionOnUpdate"] = args ? args.restartExecutionOnUpdate : undefined;
            resourceInputs["roleArn"] = args ? args.roleArn : undefined;
            resourceInputs["stages"] = args ? args.stages : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["triggers"] = args ? args.triggers : undefined;
            resourceInputs["variables"] = args ? args.variables : undefined;
            resourceInputs["version"] = undefined /*out*/;
        } else {
            resourceInputs["artifactStore"] = undefined /*out*/;
            resourceInputs["artifactStores"] = undefined /*out*/;
            resourceInputs["disableInboundStageTransitions"] = undefined /*out*/;
            resourceInputs["executionMode"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["pipelineType"] = undefined /*out*/;
            resourceInputs["restartExecutionOnUpdate"] = undefined /*out*/;
            resourceInputs["roleArn"] = undefined /*out*/;
            resourceInputs["stages"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["triggers"] = undefined /*out*/;
            resourceInputs["variables"] = undefined /*out*/;
            resourceInputs["version"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Pipeline.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Pipeline resource.
 */
export interface PipelineArgs {
    artifactStore?: pulumi.Input<inputs.codepipeline.PipelineArtifactStoreArgs>;
    artifactStores?: pulumi.Input<pulumi.Input<inputs.codepipeline.PipelineArtifactStoreMapArgs>[]>;
    disableInboundStageTransitions?: pulumi.Input<pulumi.Input<inputs.codepipeline.PipelineStageTransitionArgs>[]>;
    executionMode?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    pipelineType?: pulumi.Input<string>;
    restartExecutionOnUpdate?: pulumi.Input<boolean>;
    roleArn: pulumi.Input<string>;
    stages: pulumi.Input<pulumi.Input<inputs.codepipeline.PipelineStageDeclarationArgs>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.codepipeline.PipelineTagArgs>[]>;
    triggers?: pulumi.Input<pulumi.Input<inputs.codepipeline.PipelineTriggerDeclarationArgs>[]>;
    variables?: pulumi.Input<pulumi.Input<inputs.codepipeline.PipelineVariableDeclarationArgs>[]>;
}
