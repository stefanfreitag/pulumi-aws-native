// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::AppRunner::ObservabilityConfiguration resource  is an AWS App Runner resource type that specifies an App Runner observability configuration
 */
export class ObservabilityConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing ObservabilityConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ObservabilityConfiguration {
        return new ObservabilityConfiguration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:apprunner:ObservabilityConfiguration';

    /**
     * Returns true if the given object is an instance of ObservabilityConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ObservabilityConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ObservabilityConfiguration.__pulumiType;
    }

    /**
     * It's set to true for the configuration with the highest Revision among all configurations that share the same Name. It's set to false otherwise.
     */
    public /*out*/ readonly latest!: pulumi.Output<boolean>;
    /**
     * The Amazon Resource Name (ARN) of this ObservabilityConfiguration
     */
    public /*out*/ readonly observabilityConfigurationArn!: pulumi.Output<string>;
    /**
     * A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
     */
    public readonly observabilityConfigurationName!: pulumi.Output<string | undefined>;
    /**
     * The revision of this observability configuration. It's unique among all the active configurations ('Status': 'ACTIVE') that share the same ObservabilityConfigurationName.
     */
    public /*out*/ readonly observabilityConfigurationRevision!: pulumi.Output<number>;
    /**
     * A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
     */
    public readonly tags!: pulumi.Output<outputs.CreateOnlyTag[] | undefined>;
    /**
     * The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
     */
    public readonly traceConfiguration!: pulumi.Output<outputs.apprunner.ObservabilityConfigurationTraceConfiguration | undefined>;

    /**
     * Create a ObservabilityConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ObservabilityConfigurationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["observabilityConfigurationName"] = args ? args.observabilityConfigurationName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["traceConfiguration"] = args ? args.traceConfiguration : undefined;
            resourceInputs["latest"] = undefined /*out*/;
            resourceInputs["observabilityConfigurationArn"] = undefined /*out*/;
            resourceInputs["observabilityConfigurationRevision"] = undefined /*out*/;
        } else {
            resourceInputs["latest"] = undefined /*out*/;
            resourceInputs["observabilityConfigurationArn"] = undefined /*out*/;
            resourceInputs["observabilityConfigurationName"] = undefined /*out*/;
            resourceInputs["observabilityConfigurationRevision"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["traceConfiguration"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["observabilityConfigurationName", "tags[*]", "traceConfiguration"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(ObservabilityConfiguration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ObservabilityConfiguration resource.
 */
export interface ObservabilityConfigurationArgs {
    /**
     * A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
     */
    observabilityConfigurationName?: pulumi.Input<string>;
    /**
     * A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.CreateOnlyTagArgs>[]>;
    /**
     * The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
     */
    traceConfiguration?: pulumi.Input<inputs.apprunner.ObservabilityConfigurationTraceConfigurationArgs>;
}
