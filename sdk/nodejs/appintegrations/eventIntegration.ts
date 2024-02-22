// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppIntegrations::EventIntegration
 */
export class EventIntegration extends pulumi.CustomResource {
    /**
     * Get an existing EventIntegration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): EventIntegration {
        return new EventIntegration(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appintegrations:EventIntegration';

    /**
     * Returns true if the given object is an instance of EventIntegration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is EventIntegration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === EventIntegration.__pulumiType;
    }

    /**
     * The event integration description.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Eventbridge bus for the event integration.
     */
    public readonly eventBridgeBus!: pulumi.Output<string>;
    /**
     * The EventFilter (source) associated with the event integration.
     */
    public readonly eventFilter!: pulumi.Output<outputs.appintegrations.EventIntegrationEventFilter>;
    /**
     * The Amazon Resource Name (ARN) of the event integration.
     */
    public /*out*/ readonly eventIntegrationArn!: pulumi.Output<string>;
    /**
     * The name of the event integration.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The tags (keys and values) associated with the event integration.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a EventIntegration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: EventIntegrationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.eventBridgeBus === undefined) && !opts.urn) {
                throw new Error("Missing required property 'eventBridgeBus'");
            }
            if ((!args || args.eventFilter === undefined) && !opts.urn) {
                throw new Error("Missing required property 'eventFilter'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["eventBridgeBus"] = args ? args.eventBridgeBus : undefined;
            resourceInputs["eventFilter"] = args ? args.eventFilter : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["eventIntegrationArn"] = undefined /*out*/;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["eventBridgeBus"] = undefined /*out*/;
            resourceInputs["eventFilter"] = undefined /*out*/;
            resourceInputs["eventIntegrationArn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["eventBridgeBus", "eventFilter", "name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(EventIntegration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a EventIntegration resource.
 */
export interface EventIntegrationArgs {
    /**
     * The event integration description.
     */
    description?: pulumi.Input<string>;
    /**
     * The Amazon Eventbridge bus for the event integration.
     */
    eventBridgeBus: pulumi.Input<string>;
    /**
     * The EventFilter (source) associated with the event integration.
     */
    eventFilter: pulumi.Input<inputs.appintegrations.EventIntegrationEventFilterArgs>;
    /**
     * The name of the event integration.
     */
    name?: pulumi.Input<string>;
    /**
     * The tags (keys and values) associated with the event integration.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
